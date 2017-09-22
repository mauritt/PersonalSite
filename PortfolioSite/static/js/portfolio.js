window.onload = function(){
    console.log('a')
    projects = document.getElementsByClassName("project");
    function time_delay(i){
        var delay=200;
        return setTimeout(function(){projects[i].style.visibility = "visible";}, delay*i);
    };

    for(i=0;i<projects.length;i++){
        time_delay(i);

    };
};
