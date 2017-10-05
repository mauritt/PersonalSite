
function changePage(obj, section){
    var main = document.getElementById('main');
    var newPage = obj.innerHTML;
    var url = section + "/" + newPage + " #content";

    $(main).load(url, function(){
        var featured = document.getElementById('featured')
        if(featured){
            fillDetails(featured);
        }
    })
}


function fillDetails(obj){
    var id = obj.firstElementChild.id;
    var url = 'portfolio/details/' + id +' #details'
    $(obj).load(url);

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
