




function clickCopy(){
    var copyEmail = document.getElementById('emailCopy');
    copyEmail.select();
    copyEmail.setSelectionRange(0,9999);
    navigator.clipboard.writeText(copyEmail.value);
    Swal.fire(
        'Email Copied to clipboard'
    )
}