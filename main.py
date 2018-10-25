from readcsv import readcsv
from validate_data import validate_data, \
    DiffListLengthError, NegTimeValueError
from peak_detect import peak_detect
from time_duration import time_duration
from voltage_extremes import voltage_extremes
from count_beats import count_beats
from calc_mean_hr import calc_mean_hr
from create_dict import create_dict
from write_JSON import write_JSON


if __name__ == "__main__":
    filename = 'test_data/test_data1.csv'
    raw_data = readcsv(filename)
    validate_data(raw_data)

    beats = peak_detect(raw_data)
    duration = time_duration(raw_data)
    voltage_extremes = voltage_extremes(raw_data)
    num_beats = count_beats(beats)
    mean_hr_bpm = calc_mean_hr(num_beats, duration)
    metrics = create_dict(mean_hr_bpm, voltage_extremes, duration,
                          num_beats, beats)
    print(metrics)
    write_JSON(mean_hr_bpm, 'test_data1')
