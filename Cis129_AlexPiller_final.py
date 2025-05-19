START SERVER
  INITIALIZE web framework
  INITIALIZE real-time communication
  SET UP directory for storing uploaded images

  DEFINE route: '/'
    RENDER chat page (HTML)

  DEFINE route: '/upload'
    IF file is received:
      SAVE file to upload directory
      BROADCAST image filename to all clients

  DEFINE WebSocket event: 'text'
    WHEN text message is received:
      BROADCAST message to all clients

  START server with real-time support

ON PAGE LOAD:
  CONNECT to server

  WHEN 'text' message is received:
    DISPLAY message in chat area

  WHEN 'image' message is received:
    DISPLAY image in chat area using image URL

  ON user input text and press "Send":
    EMIT 'text' event with message and user info to server

  ON user select image and press "Send Image":
    SEND image file to server using file upload

FUNCTION displayText(user, message):
    SHOW user name and message

FUNCTION displayImage(filename):
  ADD image tag to chat area with source:
    "/uploads/" + filename

