def fetch_server_data(query):
    import requests

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-GB,en;q=0.6',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    url = f"https://servers-frontend.fivem.net/api/servers/single/{query}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'Data' in data:
            ip = data['Data'].get('connectEndPoints', ['N/A'])[0]
            mxclients = data['Data'].get('sv_maxclients', 'N/A')
            clients = data['Data'].get('clients', 'N/A')
            hostname = data['Data'].get('hostname', 'N/A')
            upvotepower = data['Data'].get('upvotePower', 'N/A')
            ownername = data['Data'].get('ownerName', 'N/A')
            ownerprofile = data['Data'].get('ownerProfile', 'N/A')
            discord_link = data['Data']['vars'].get('Discord', 'N/A')
            return f"""IP: {ip} \nMax Clients: {mxclients} \nClients: {clients} \nHostname: {hostname} \nUpvote Power: {upvotepower} \nOwner Name: {ownername} \nOwner Profile: {ownerprofile} \nDiscord: {discord_link}"""
        else:
            return "No server found"

    except requests.RequestException as e:
        return f"Error: {e}"
    except ValueError:
        return "Failed to decode JSON"