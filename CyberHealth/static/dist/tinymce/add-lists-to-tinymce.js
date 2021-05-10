
(function($){
    alert(1);
    tinymce.activeEditor.execCommand('InsertOrderedList', false, {
      'list-style-type': 'decimal',
      'list-item-attributes': {class: 'govuk-list--number'}
    });
    tinymce.activeEditor.execCommand('InsertUnorderedList', false, {
      'list-style-type': 'disc',
      'list-item-attributes': {class: 'govuk-list--bullet'}
    });
});