function run_cnm_pipeline()
%RUN_CNM_PIPELINE Dummy MATLAB entry point mirroring src/python/run_pipeline.py.
%
%   From repo root:
%     addpath('src/matlab');
%     run_cnm_pipeline

    repoRoot = fileparts(fileparts(fileparts(mfilename('fullpath'))));
    outDir = fullfile(repoRoot, 'data', '02_processed');
    if ~isfolder(outDir)
        mkdir(outDir);
    end

    fprintf('CNM MATLAB pipeline\n');
    fprintf('Output: %s\n\n', outDir);

    if isfile(fullfile(repoRoot, 'datasets', 'march8.csv')) || ...
            isfile(fullfile(repoRoot, 'data', '01_raw', 'march8.csv'))
        T = load_cnm_data('march8.csv');
        summary = table( ...
            {'march8.csv'}, ...
            max(T.ids(T.vgs == max(T.vgs))), ...
            min(T.ids(T.vgs == min(T.vgs))), ...
            height(T), ...
            'VariableNames', {'source_file', 'ids_on_a', 'ids_off_a', 'n_points'});
        writetable(summary, fullfile(outDir, 'iv_summary_matlab.csv'));
        fprintf('Wrote iv_summary_matlab.csv\n');
    end

    if isfile(fullfile(repoRoot, 'datasets', 'noise_NEW2.dat')) || ...
            isfile(fullfile(repoRoot, 'data', '01_raw', 'noise_NEW2.dat'))
        plot_noise_spectrum('noise_NEW2.dat');
        fprintf('Opened noise spectrum figure.\n');
    end

    fprintf('\nMATLAB pipeline complete.\n');
end
