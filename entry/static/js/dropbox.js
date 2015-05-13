function dropbox(dropboxDIV,postURL) {

    var oDropBox = document.getElementById(dropboxDIV);
    var navbarImg = document.getElementById('navbar');
    var percentageDataDIV = document.getElementById('percentage');
    oDropBox.addEventListener('dragover', function(e) {
        e.stopPropagation();
        e.preventDefault();
    }, false);
    oDropBox.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        e.stopPropagation();
        e.preventDefault();

        var fileList  = e.dataTransfer.files;
        fileType = fileList[0].type;
        oImg = document.createElement('img');
        reader = new FileReader();

        oImg.className='img-responsive';

        if (fileType.indexOf('image') != -1) {
            reader.onload = function(e) {
                oImg.src = this.result;
                navbarImg.appendChild(oImg);

            }
        }else{

        }
        reader.readAsDataURL(fileList[0]);
        uploadState =uploadFile(fileList[0],postURL);  

        return uploadState;
    }
}

function uploadFile(file,postURL) {

        			// prepare XMLHttpRequest
        var xhr = new XMLHttpRequest();
        var navbar = document.getElementById('navbar');
        var percentageDIV = document.createElement("div");
        


        percentageDIV.style.background="#E44B23";
        percentageDIV.style.height="1px";
        navbar.appendChild(percentageDIV)

        //xhr.open('POST', '/dropbox/');
       xhr.onload = function() {
            //result.innerHTML += this.responseText;
            //handleComplete(file.size);

        };
        xhr.addEventListener("progress",function(e){
            if(e.lengthComputable){
                var percentage =Math.round((e.loaded * 100)/e.total);

                percentageDIV.innerHTML=percentage+'%';
                
                
                
            }
        },false);
        
        uploadUrlDiv = document.getElementById('upload-url');
        xhr.addEventListener("load",function(e){
            alert(e.target.responseText);
            var name = e.target.responseText;
            //uploadUrlDiv = document.getElementById("upload-url");
            uploadUrlDiv.innerHTML='<a href="http://7xj0ss.com1.z0.glb.clouddn.com/'+name+'">'+name+'</a>';
        },false);
        // prepare FormData
        var formData = new FormData();
        xhr.open('POST', postURL);
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest"); 
        
        formData.append('fileContent', file);
        formData.append('filename',file.name);
        xhr.send(formData);
        
        return 1;

}
