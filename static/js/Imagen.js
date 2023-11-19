const expandImg = (image) => {
    let img = document.getElementById(image);
    let width = img.width;
    let height = img.height;
    if(width == 640 && height == 480) {
        img.width = '1280';
        img.height = '1024';
    } else {
        img.width = '640';
        img.height = '480';
    }
}

