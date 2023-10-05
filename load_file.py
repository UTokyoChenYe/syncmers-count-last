def read_noverlap_results(file_path, filename):
    """Reads the results of a noverlap experiment from a file.And returns a list of the results.

    Args:
        file_path (str): The path to the file.
        filename (str): The name of the file to read from.

    Returns:
        result_list(list): The results of the experiment.
    """
    result_list = []
    with open(file_path + '/'+filename, 'r') as f:
        for line in f:
            result_list.append(line.strip())
    return result_list