function T = load_cnm_data(filename)
%LOAD_CNM_DATA Load a CNM CSV or whitespace-delimited DAT file.
%
%   T = load_cnm_data('march8.csv')
%   T = load_cnm_data('noise_NEW2.dat')

    repoRoot = fileparts(fileparts(fileparts(mfilename('fullpath'))));
    dataDir = fullfile(repoRoot, 'datasets');
    if ~isfolder(dataDir)
        dataDir = fullfile(repoRoot, 'data', '01_raw');
    end

    filepath = fullfile(dataDir, filename);
    [~, ~, ext] = fileparts(filename);

    switch lower(ext)
        case '.csv'
            T = readtable(filepath);
        case '.dat'
            T = read_cnm_dat(filepath);
        otherwise
            error('load_cnm_data:UnsupportedFormat', 'Unsupported extension: %s', ext);
    end
end

function T = read_cnm_dat(filepath)
    raw = fileread(filepath);
    lines = splitlines(raw);
    rows = {};
    for i = 1:numel(lines)
        line = strtrim(lines{i});
        if isempty(line) || startsWith(line, '#')
            continue;
        end
        rows{end+1} = split(line); %#ok<AGROW>
    end

    header = rows{1};
    data = vertcat(rows{2:end});
    numeric = cellfun(@str2double, data, 'UniformOutput', false);
    T = cell2table(numeric, 'VariableNames', header);
end
