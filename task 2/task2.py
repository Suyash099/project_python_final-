import sys

def read_log_file(file_path):
    """
    Read and parse the log file.

    Parameters:
    file_path (str): Path to the log file.

    Returns:
    list: Parsed data from the log file.
    """
    with open(file_path, "r") as file:
        return [line.strip().split(',') for line in file.readlines()]

def analyze_cat_visits(data):
    """
    Analyze cat visit data to count visits, calculate total, longest, and shortest visit times.

    Parameters:
    data (list): Parsed cat visit data.

    Returns:
    tuple: Calculated statistics (our cat count, other cat count, total time, longest visit, shortest visit).
    """
    count_our_cat, count_their_cat, total_time, longest_visit, shortest_visit = 0, 0, 0, 0, float('inf')

    for record in data:
        if record[0] == 'THEIRS':
            count_their_cat += 1
        elif record[0] == 'OURS':
            count_our_cat += 1
            time_stayed = int(record[2]) - int(record[1])
            total_time += time_stayed

            longest_visit = max(longest_visit, time_stayed)
            shortest_visit = min(shortest_visit, time_stayed)

    return count_our_cat, count_their_cat, total_time, longest_visit, shortest_visit

def print_statistics(our_cat, their_cat, total_time, longest_visit, shortest_visit):
    """
    Print the analyzed statistics of cat visits.

    Parameters:
    our_cat (int): Count of our cat's visits.
    their_cat (int): Count of other cats' visits.
    total_time (int): Total time of our cat's visits in minutes.
    longest_visit (int): Longest visit time in minutes.
    shortest_visit (int): Shortest visit time in minutes.
    """
    print("Log File Analysis")
    print("=" * len("Log File Analysis"))
    print(f"\nCat Visits: {our_cat}")
    print(f"Other Cats: {their_cat}")
    print(f"Total Time in House: {total_time//60} Hours, {total_time%60} Minutes")
    if our_cat > 0:
        print(f"\nAverage Visit Length: {total_time//our_cat} Minutes")
    else:
        print("Average Visit Length: No visits from our cat")
    print(f"Longest Visit: {longest_visit} Minutes")
    print(f"Shortest Visit: {shortest_visit if shortest_visit != float('inf') else 'N/A'} Minutes")

def main():
    """
    Main function to process cat visit log file and print statistics.
    """
    try:
        log_file_path = sys.argv[1]
        data = read_log_file(log_file_path)
        stats = analyze_cat_visits(data)
        print_statistics(*stats)

    except IndexError:
        print("Missing command line argument.")
    except FileNotFoundError:
        print(f"Cannot open '{log_file_path}'!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()