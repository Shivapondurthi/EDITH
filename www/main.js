$(document).ready(function () {

    let i=0;

    $('.heading').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-msg').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#micbutton").click(function(){
        if (i==0){
            eel.play_sound()
            i+=1
        }
        $("#Oval-Section").attr("hidden", true);
        $("#SiriWave-Section").attr("hidden", false);
        
        eel.allCommands()()
       
        
    });


    


});