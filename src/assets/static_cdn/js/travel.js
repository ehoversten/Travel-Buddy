// 'use strict';
// $(document).ready(function() {
//   $(document).on('submit', '.form-destination-ajax', function(e) {
//     e.preventDefault();
//     console.log('working');
//     let thisForm = $(this);
//     let httpMethod = thisForm.attr('method');
//     let actionEndPoint = thisForm.attr('data-endpoint');
//     let formData = thisForm.serialize()
//     $.ajax({
//       url: actionEndPoint,
//       method: httpMethod,
//       data: formData,
//       success: function(data) {
//         console.log(data);
//       },
//       error: function(errorData) {
//         $.alert({
//           title: 'Ooops',
//           content: 'An error ocurred',
//           theme: 'modern'
//         });
//         console.log(errorData);
//       }
//     });
//   });
// });
