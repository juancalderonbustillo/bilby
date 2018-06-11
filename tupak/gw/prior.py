import logging


def test_redundancy(key, prior):
    """
    Test whether adding the key would add be redundant.

    Parameters
    ----------
    key: str
        The string to test.
    prior: dict
        Current prior dictionary.

    Return
    ------
    redundant: bool
        Whether the key is redundant
    """
    redundant = False
    mass_parameters = {'mass_1', 'mass_2', 'chirp_mass', 'total_mass', 'mass_ratio', 'symmetric_mass_ratio'}
    spin_magnitude_parameters = {'a_1', 'a_2'}
    spin_tilt_1_parameters = {'tilt_1', 'cos_tilt_1'}
    spin_tilt_2_parameters = {'tilt_2', 'cos_tilt_2'}
    spin_azimuth_parameters = {'phi_1', 'phi_2', 'phi_12', 'phi_jl'}
    inclination_parameters = {'iota', 'cos_iota'}
    distance_parameters = {'luminosity_distance', 'comoving_distance', 'redshift'}

    for parameter_set in [mass_parameters, spin_magnitude_parameters, spin_azimuth_parameters]:
        if key in parameter_set:
            if len(parameter_set.intersection(prior.keys())) > 2:
                redundant = True
                logging.warning('{} in prior. This may lead to unexpected behaviour.'.format(
                    parameter_set.intersection(prior.keys())))
                break
            elif len(parameter_set.intersection(prior.keys())) == 2:
                redundant = True
                break
    for parameter_set in [inclination_parameters, distance_parameters, spin_tilt_1_parameters, spin_tilt_2_parameters]:
        if key in parameter_set:
            if len(parameter_set.intersection(prior.keys())) > 1:
                redundant = True
                logging.warning('{} in prior. This may lead to unexpected behaviour.'.format(
                    parameter_set.intersection(prior.keys())))
                break
            elif len(parameter_set.intersection(prior.keys())) == 1:
                redundant = True
                break

    return redundant