$(document).ready(function(){

    //Display speak message
    eel.expose(DisplayMessage)
    function DisplayMessage(message){
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate("start")
    }
})