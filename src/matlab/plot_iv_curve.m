function plot_iv_curve(filename)
%PLOT_IV_CURVE Dummy IV plot from a CNM CSV export.
%
%   plot_iv_curve('march8.csv')

    T = load_cnm_data(filename);

    figure('Name', ['IV — ' filename]);
    if all(ismember({'vgs', 'ids'}, T.Properties.VariableNames))
        plot(T.vgs, T.ids, '-o', 'LineWidth', 1.5);
        xlabel('V_{GS} (V)');
        ylabel('I_{DS} (A)');
        set(gca, 'YScale', 'log');
    elseif all(ismember({'v', 'i'}, T.Properties.VariableNames))
        plot(T.v, T.i, '-o', 'LineWidth', 1.5);
        xlabel('V (V)');
        ylabel('I (A)');
    else
        error('plot_iv_curve:MissingColumns', 'No recognised IV columns in %s', filename);
    end
    grid on;
    title(['IV curve — ' filename]);
end
