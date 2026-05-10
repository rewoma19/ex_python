"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    Parameters:
        temperature (int or float): The temperature value in kelvin.
        neutrons_emitted (int or float): The number of neutrons emitted per second.

    Returns:
        bool: Is criticality balanced?

    Note:
        A reactor is said to be balanced in criticality if it satisfies the following conditions:
            - The temperature is less than 800 K.
            - The number of neutrons emitted per second is greater than 500.
            - The product of temperature and neutrons emitted per second is less than 500000.

    """

    temp_is_right = temperature < 800
    neutron_emission_is_right = neutrons_emitted > 500
    product_of_neutrons_and_temp = temperature * neutrons_emitted

    return temp_is_right and neutron_emission_is_right and (product_of_neutrons_and_temp < 500000)

print(is_criticality_balanced(750, 600))


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    Parameters:
        voltage (int or float): Voltage value.
        current (int or float): Current value.
        theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    Returns:
        str: One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        where generated power = voltage * current
    """

    efficiency_band = ""
    generated_power = voltage * current
    efficiency_as_percent = (generated_power / theoretical_max_power) * 100

    if efficiency_as_percent < 30:
        efficiency_band = "black"
    elif 30 <= efficiency_as_percent < 60:
        efficiency_band = "red"
    elif 60 <= efficiency_as_percent < 80:
        efficiency_band = "orange"
    else:
        efficiency_band = "green"

    return efficiency_band

print(reactor_efficiency(200,50,15000))

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    status_code = ""
    product_of_temp_and_neutrons = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold


    if product_of_temp_and_neutrons < (0.9 * threshold):
        status_code = "LOW"
    elif lower_bound <= product_of_temp_and_neutrons <= upper_bound:
        status_code = "NORMAL"
    else:
        status_code = "DANGER"

    return status_code

print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))

