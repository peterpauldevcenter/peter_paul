// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        read: function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/student',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(first_name, last_name) {
            let ajax_options = {
                type: 'POST',
                url: 'api/student',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'first_name': first_name,
                    'last_name': last_name
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(first_name, last_name, student_id) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/student/' + student_id,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'student_id': student_id,
                    'first_name': first_name,
                    'last_name': last_name
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        delete: function(student_id) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/student/' + student_id,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $first_name = $('#first_name'),
        $last_name = $('#last_name'),
        $student_id = $('#student_id');

    // return the API
    return {
        reset: function() {
            $last_name.val('');
            $first_name.val('').focus();
        },
        update_editor: function(first_name, last_name, student_id) {
            $student_id.val(student_id);
            $last_name.val(last_name);
            $first_name.val(first_name).focus();
        },
        build_table: function(students) {
            let rows = ''

            // clear the table
            $('.students table > tbody').empty();

            // did we get a student array?
            if (students) {
                for (let i=0, l=students.length; i < l; i++) {
                    rows += `<tr>
                                 <td class="student_id">${students[i].student_id}</td>
                                 <td class="first_name">${students[i].first_name}</td>
                                 <td class="last_name">${students[i].last_name}</td>
                             </tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $first_name = $('#first_name'),
        $last_name = $('#last_name'),
        $student_id = $('#student_id');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(first_name, last_name, student_id) {
        return first_name !== "" && last_name !== "" && student_id !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let first_name = $first_name.val(),
            last_name = $last_name.val();

        e.preventDefault();

        if (validate(first_name, last_name, 'placeholder')) {
            model.create(first_name, last_name)
        } else {
            alert('Problem with first or last name input');
        }
    });

    $('#update').click(function(e) {
        let first_name = $first_name.val(),
            last_name = $last_name.val(),
            student_id = $student_id.val();

        e.preventDefault();

        if (validate(first_name, last_name, student_id)) {
            model.update(first_name, last_name, student_id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let student_id = $student_id.val();

        e.preventDefault();

        if (validate('placeholder', 'placeholder', student_id)) {
            model.delete(student_id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            first_name,
            last_name,
            student_id;

        first_name = $target
            .parent()
            .find('td.first_name')
            .text();

        last_name = $target
            .parent()
            .find('td.last_name')
            .text();

        student_id = $target
            .parent()
            .find('td.student_id')
            .text();

        view.update_editor(first_name, last_name, student_id);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));
