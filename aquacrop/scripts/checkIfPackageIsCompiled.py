from subprocess import call


def compile_all_AOT_files():
    """
    Numba AOT compile functions to improve speed
    
    """
    try:
        from ..solution.aeration_stress import aeration_stress
        from ..solution.water_stress import water_stress
        from ..solution.evap_layer_water_content import (
            evap_layer_water_content,
        )
        from ..solution.root_zone_water import root_zone_water
        from ..solution.cc_development import cc_development
        from ..solution.update_CCx_CDC import update_CCx_CDC
        from ..solution.cc_required_time import cc_required_time
        from ..solution.temperature_stress import temperature_stress
        from ..solution.HIadj_pre_anthesis import HIadj_pre_anthesis
        from ..solution.HIadj_post_anthesis import HIadj_post_anthesis
        from ..solution.HIadj_pollination import HIadj_pollination
        from ..solution.growing_degree_day import growing_degree_day
        from ..solution.drainage import drainage
        from ..solution.rainfall_partition import rainfall_partition
        from ..solution.check_groundwater_table import check_groundwater_table
        from ..solution.soil_evaporation import soil_evaporation
        from ..solution.root_development import root_development
        from ..solution.infiltration import infiltration
        from ..solution.HIref_current_day import HIref_current_day
        from ..solution.biomass_accumulation import biomass_accumulation

    except:
        pass
