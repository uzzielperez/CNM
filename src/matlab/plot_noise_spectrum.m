function plot_noise_spectrum(filename)
%PLOT_NOISE_SPECTRUM Dummy log-log noise plot from a CNM .dat export.
%
%   plot_noise_spectrum('noise_NEW2.dat')

    T = load_cnm_data(filename);

    figure('Name', ['Noise — ' filename]);
    loglog(T.freq, T.Sv, '-o', 'LineWidth', 1.5);
    xlabel('Frequency (Hz)');
    ylabel('S_v (V^2/Hz)');
    grid on;
    title(['Voltage noise spectrum — ' filename]);
end
