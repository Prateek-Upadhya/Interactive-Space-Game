# Computer-Vision-Game

![game snap](https://github.com/Prateek-Upadhya/Interactive-Space-Game/blob/main/game_snap.jpg?raw=true)


- This project aims to build a space game with a twist. Instead of using conventional keyboard controls, we intend to use OpenCV assets for Unity and integrate a hand-motion control mechanism that will allow users to interact with the game.

![hand tracking](https://github.com/Prateek-Upadhya/Interactive-Space-Game/blob/main/hand_track.jpg?raw=true)

- It uses the Google Mediapipe Hands API to perform real time hand-tracking. Gestures and movements are tracked using the 21 - landmark coordinates returned by the model. The positional data of the hand is transmitted to the Unity-based game using a UDP connection. The server code is written in python while the client code is written in C# and embedded into the game scripts. 

- A Datagram Socket was implemented and UDP was chosen as the frequency of receving packets about the hand coordinates is more important than the reliability and gaurentee of arrival. 
