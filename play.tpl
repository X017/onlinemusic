<html> 

<button> Play </button>
music <input name="music_name" type="text">

<%
	from pygame import mixer
	mixer.init()
	mixer.music.load('/music' + {{music_name}})
	
%>
</html>
