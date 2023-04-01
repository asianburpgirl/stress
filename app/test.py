import neurokit2 as nk
import matplotlib.pyplot as plt
import random
def getEcg():
    # Generate synthetic ECG signal
    #ecg = nk.ecg_simulate(duration=10, heart_rate=70,sampling_rate=50,drift=0.01 ,noise=0.05)
    # Generate 15 seconds of ECG signal (recorded at 250 samples / second)
    ecg = nk.ecg_simulate(duration=15, sampling_rate=250, heart_rate=random.randint(70,85))
    # Plot ECG signal
    #nk.signal_plot(ecg)
    #plt.show()
    # Extract R-peaks
    rpeaks = nk.ecg_peaks(ecg, sampling_rate=250)[1]
    # # Compute heart rate variability indices
    hrv = nk.hrv_time(rpeaks, sampling_rate=250)
    # print(hrv)


    # Process it
    #signals, info = nk.ecg_process(ecg, sampling_rate=250)

    # Visualise the processing
    #nk.ecg_plot(signals, sampling_rate=250)
    return float(hrv["HRV_SDNN"] * 8)
    #print(hrv)
    #Print results
    # plt.plot(ecg)
    # plt.xlabel('Time (s)')
    # plt.ylabel('Amplitude')
    #plt.show()
def ecg2():
    hr = random.randint(70,85)
    ecg = nk.ecg_simulate(duration=15, sampling_rate=100, heart_rate=hr, random_state=333)

    # Process it
    signals, info = nk.ecg_process(ecg, sampling_rate=100)
    rpeaks = nk.ecg_peaks(ecg, sampling_rate=100)[1]
    # # Compute heart rate variability indices
    hrv = nk.hrv_time(rpeaks, sampling_rate=100)
    # Visualise the processing
    #nk.ecg_plot(signals, sampling_rate=250)
    # Save it
    #plt.plot(signals["ECG_Clean"])
    return (float(hrv["HRV_SDNN"]) * 8.1,hr)
#ecg2()
# data = []
# SDNN = []
# for i in range(1,21):
#     temp = ecg2()
#     data.append([str(i) + "/3/2023",temp])
#     SDNN.append(temp)
# plt.plot(SDNN)
# plt.show()