
#include <AMReX.H>
#include <AMReX_ParmParse.H>
#include <AMReX_ParallelDescriptor.H>
#include <AMReX_Amr.H>

#include <CNS.H>

using namespace amrex;

void initialize_EBIS(const int max_level);

int main (int argc, char* argv[])
{
    amrex::Initialize(argc,argv);

    BL_PROFILE_VAR("main()", pmain);

    Real timer_tot = ParallelDescriptor::second();
    Real timer_init = 0.;
    Real timer_advance = 0.;
    Real timer_loadbalance = 0.;

    int  max_step;
    Real strt_time;
    Real stop_time;

    {
        ParmParse pp; 

        max_step  = -1;
        strt_time =  0.0;
        stop_time = -1.0;

        pp.query("max_step",max_step);
        pp.query("strt_time",strt_time);
        pp.query("stop_time",stop_time);
    }

    if (strt_time < 0.0) {
        amrex::Abort("MUST SPECIFY a non-negative strt_time"); 
    }

    if (max_step < 0 && stop_time < 0.0) {
	amrex::Abort("Exiting because neither max_step nor stop_time is non-negative.");
    }

    {
        timer_init = ParallelDescriptor::second();

	Amr amr;

        //xxxxx This can be done in the constructor of Amr
        initialize_EBIS(amr.maxLevel());

	amr.init(strt_time,stop_time);

        timer_init = ParallelDescriptor::second() - timer_init;

        timer_advance = ParallelDescriptor::second();

	while ( amr.okToContinue() &&
  	       (amr.levelSteps(0) < max_step || max_step < 0) &&
	       (amr.cumTime() < stop_time || stop_time < 0.0) )
	    
	{
            if (CNS::do_load_balance) {
                Real t0 = ParallelDescriptor::second();
                CNS::LoadBalance(amr);
                timer_loadbalance += ParallelDescriptor::second()-t0;
            }

	    //
	    // Do a coarse timestep.  Recursively calls timeStep()
	    //
	    amr.coarseTimeStep(stop_time);
	}
	
        timer_advance = ParallelDescriptor::second() - timer_advance;

	// Write final checkpoint and plotfile
	if (amr.stepOfLastCheckPoint() < amr.levelSteps(0)) {
	    amr.checkPoint();
	}
	
	if (amr.stepOfLastPlotFile() < amr.levelSteps(0)) {
	    amr.writePlotFile();
	}
    }

    timer_tot = ParallelDescriptor::second() - timer_tot;

    ParallelDescriptor::ReduceRealMax({timer_tot, timer_init, timer_advance, timer_loadbalance},
                                      ParallelDescriptor::IOProcessorNumber());

    amrex::Print() << "Run Time total        = " << timer_tot     << "\n"
                   << "Run Time init         = " << timer_init    << "\n"
                   << "Run Time advance      = " << timer_advance << "\n";
    if (CNS::do_load_balance) {
        amrex::Print() << "Run time load balance = " << timer_loadbalance << "\n";
    }

    BL_PROFILE_VAR_STOP(pmain);

    amrex::Finalize();

    return 0;
}
