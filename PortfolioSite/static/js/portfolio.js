function show_project(obj, proj_id){
    screen = document.getElementById("screen");
    screen.style.visibility ="visible";
    screen.style.opacity = ".90";
    lightbox = document.getElementById("lightbox");

    $(lightbox).load("/portfolio/detail/" + proj_id + " #details");

    lightbox.style.visibility="visible";

    lightbox.style.opacity = "1";
};

function hide_video(){
    var screen = document.getElementById('screen');
    screen.style.opacity = "0"
    screen.style.visibility = "hidden";
    var x = document.getElementById('closeButton');
    x.style.opacity = "0"
    x.style.visibility = "hidden";
    var lightbox = document.getElementById("lightbox");
    var embed = document.getElementById("details");
    lightbox.style.opacity = "0"
    lightbox.style.visibility="hidden";
    lightbox.removeChild(embed);
};


function swapLogo(obj,imagePath){
    var newPath = obj.src.split('/');
    newPath.pop();
    newPath = newPath.join('/') + '/' + imagePath

    obj.src=newPath;

}

function activatePage(){
    var navList = document.getElementById("siteNav").firstElementChild
    var pageName = navList.id;
    var listItems = navList.getElementsByTagName('li');

    for (var i = 0; i < listItems.length; i++) {
        var link = listItems[i].firstElementChild
        var linkName = link.innerHTML;

        $(link).toggleClass('inactive', (linkName==pageName));

    };
};


window.onload = function(){

    activatePage();

    var projects = document.getElementsByClassName("project");

    function time_delay(i){
        var delay=200;
        return setTimeout(function(){
            projects[i].style.display = "inline";

        }, delay*i);
    };

    for(i=0;i<projects.length;i++){
        time_delay(i);

    };
};


