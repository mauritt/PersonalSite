
function changePage(obj, section){
    var main = getElementById('Main');
    var newPage = obj.innerHTML;
    var url = './' + section + '/' + newPage;

    $(main).load(url + " #project")
}

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

