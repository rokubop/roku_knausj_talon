# from obswebsocket import obsws, requests

# # Function to toggle the virtual camera in OBS
# def toggle_virtual_camera():
#     HOST = "localhost"  # The host where OBS WebSocket server is running
#     PORT = 4444         # The default port for OBS WebSocket server

#     # Initialize the WebSocket client and connect to OBS
#     ws = obsws(HOST, PORT)
#     ws.connect()

#     try:
#         # Check if the virtual camera is currently active
#         vc_status = ws.call(requests.GetVirtualCamStatus()).getVirtualCam()
#         if vc_status:
#             # If the virtual camera is active, stop it
#             ws.call(requests.StopVirtualCam())
#             print("Virtual Camera Stopped.")
#         else:
#             # If the virtual camera is not active, start it
#             ws.call(requests.StartVirtualCam())
#             print("Virtual Camera Started.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Always close the connection
#         ws.disconnect()
