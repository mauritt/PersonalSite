
function changePage(obj, section){
    var main = document.getElementById('main');
    var newPage = obj.innerHTML;
    var url = section + "/" + newPage + " #content";

    $(main).load(url, function(){
        if(newPage == "Video" || newPage=="Code"){
            var thumbnailList = document.getElementById('thumbnails');
            var image = thumbnailList.firstElementChild.firstElementChild;
            fillDetails(image);
        };
    });
};


function fillDetails(obj){

    var currentDetails = document.getElementById('details');
    if (currentDetails){
        var currentID = currentDetails.firstElementChild.id;
        currentID = currentID.split('_')[1]

        addThumbnail(currentID);
    };


    removeThumbnail(obj.id);

    var featured = document.getElementById('featured');
    var url = 'portfolio/details/' + obj.id + ' #details';
    $(featured).load(url);

};


function addThumbnail(id){
    var thumbnailItem = document.getElementById(id).parentElement;
    thumbnailItem.style.display = "inline"

}


function removeThumbnail(id){
    var thumbnailItem = document.getElementById(id).parentElement;
    thumbnailItem.style.display = "none"

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

function sent(){
    var contact = document.getElementById('contactForm')
    $(contact).load("contactpage/sent #successMessage")
}





