import asyncio
import websockets

# Maintain a list of connected clients
connected_clients = set()

async def handle_connection(websocket, path):
    # Add the client to the connected_clients set
    connected_clients.add(websocket)
    
    try:
        while True:
            # Wait for a message from the client
            message = await websocket.recv()
            print(message)
            # Broadcast the received message to all connected clients
            for client in connected_clients:
                await client.send(message)
    
    finally:
        # Remove the client from the connected_clients set
        connected_clients.remove(websocket)

# Start the WebSocket server
start_server = websockets.serve(handle_connection, 'localhost', 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
