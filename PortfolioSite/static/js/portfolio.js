function show_video(obj, proj_id){
    screen = document.getElementById("screen");
    screen.style.visibility ="visible";
    screen.style.opacity = ".75";
    lightbox = document.getElementById("lightbox");

    $(lightbox).load("../detail/" + proj_id + " #details");

    lightbox.style.visibility="visible";

    lightbox.style.opacity = "1";
};

function hide_video(obj){
    obj.style.opacity = "0"
    obj.style.visibility = "hidden";
    lightbox = document.getElementById("lightbox");
    embed = document.getElementById("details");
    lightbox.style.opacity = "0"
    lightbox.style.visibility="hidden";
    lightbox.removeChild(embed);
};



window.onload = function(){
    projects = document.getElementsByClassName("project");
    function time_delay(i){
        var delay=200;
        return setTimeout(function(){projects[i].style.visibility = "visible";}, delay*i);
    };

    for(i=0;i<projects.length;i++){
        time_delay(i);

    };
};
