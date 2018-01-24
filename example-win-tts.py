import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Muy buenas tardes estimada clientela, aqui esta su pedido................. que tenga un buen provecho")

