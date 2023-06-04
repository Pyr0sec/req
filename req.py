import argparse
import requests

def send_request(file_path, times, printcode):
    with open(file_path, 'r') as file:
        request_data = file.read().strip()

    lines = request_data.split('\n')
    method = lines[0].split(' ')[0]
    path = lines[0].split(' ')[1]
    url = 'https://' + lines[1].split(': ')[1] + path

    headers = {}
    for line in lines[1:]:
        if line.strip():
            key, value = line.split(': ')
            headers[key] = value
    
    for i in range(times):
        response = requests.request(method, url, headers=headers)
        if printcode:
            print(response.status_code)
        
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send custom HTTP requests from a file multiple times.')
    parser.add_argument('-f', '--file', required=True, help='Path to the request file')
    parser.add_argument('-t', '--times', type=int, default=1, help='Number of times to send the request (default: 1)')
    parser.add_argument('-p', '--printcode', help='Prints status code for each request', action='store_true', default=False)
    args = parser.parse_args()

    if args.file and args.times and args.printcode:
        send_request(args.file, args.times, printcode=1)
    elif args.file and args.times:
        send_request(args.file, args.times, printcode=0)
    elif args.file and args.printcode:
        send_request(args.file, 1, printcode=1)
    else:
        parser.print_help()