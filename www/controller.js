$(document).ready(function(){

    //Display speak message
    eel.expose(DisplayMessage)
    function DisplayMessage(message){
       
        $(".siri-msg li:first").text(message);
        $(".siri-msg").textillate("start")
    }

    eel.expose(showhood)
    function showhood(){
        $("#Oval-Section").attr("hidden", false);
        $("#SiriWave-Section").attr("hidden", true);
    }
})