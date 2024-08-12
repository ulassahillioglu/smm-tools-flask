const inputLink = document.getElementById('input_link');
const clearButton = document.getElementById('clear_button');
const copyButton = document.getElementById('copy_button');
const copyText = document.getElementById('result');

clearButton.addEventListener('click', function () {
    inputLink.value = '';
});

copyButton.addEventListener('click', function () {
    const textToCopy = copyText.textContent || copyText.innerText;

    if (navigator.clipboard) {
        navigator.clipboard.writeText(textToCopy).then(function() {
            console.log('Text copied to clipboard');
        }).catch(function(err) {
            console.error('Could not copy text: ', err);
        });
    } else {
        const tempTextArea = document.createElement('textarea');
        tempTextArea.value = textToCopy;
        document.body.appendChild(tempTextArea);
        tempTextArea.select();
        document.execCommand('copy');
        document.body.removeChild(tempTextArea);
    }
});