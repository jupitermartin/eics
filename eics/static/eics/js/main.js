function datetime_validator(str) {
    let date_regex = /^(0[1-9]|1\d|2\d|3[01])\/(0[1-9]|1[0-2])\/(19|20|21)\d{2}\s(0[0-9]|1[0-9]|2[0-3]):([0-5]\d)$/;
    return date_regex.test(str);
}

function email_validator(email_list) {
    let data_regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    let email_array = email_list.split(';');

    let flag = 1;
    for (var i=0;i < email_array.length;i++) {
        if (email_array[i] === '') {continue;}
        if (!data_regex.test(email_array[i])){
            flag = 0;
            break;
        }
    }
    return flag;
}
function onchange_enddate() {
    let start_date = $('#start_date').val();
    if (!datetime_validator(start_date)) {
        alert('Start date pattern is not correct');
        return;
    }
    let end_date = $('#end_date').val();
    if (!datetime_validator(end_date)) {
        alert('End date pattern is not correct');return;
    }
    let param = {};
    param.start_date = start_date;
    param.end_date = end_date;
    console.log(param);
    $.ajax({
        type: 'POST',
        url: '/calc_duration',
        data: param,
        success: function (res) {
            if (res === 'timeformaterror') {
                console.log('Date time is not correct');
                return;
            } else {
                let res_ = JSON.parse(res);
                let hours = res_['hours'];
                let mins = res_['mins'];
                $('#duration').val(hours + ":" + mins);
            }
        }
    });
}
function onchange_startdate() {
    let start_date = $('#start_date').val();
    if (!datetime_validator(start_date)) {
        alert('Start date pattern is not correct');
    }
}
function onback() {
    window.location.href = '/';
}
function onchange_splice_number() {
    let splice_num = $('#splice_number').val();
    if (splice_num === '-1') {
        return;
    }
    let param = {'splice_num': splice_num};
    console.log(param);
    $('#auto_loading_fields').html('');
    $('#auto_loading_fields').load('/auto_load_extra', param);
}

function onclick_cp_submit() {
    let to_addresses = $('#to_addresses').val();
    if (to_addresses === '') {
        alert('Please fill to addresses');return;
    }
    if (!email_validator(to_addresses)) {
        alert('One of emails of to addresses has incorrect pattern');return;
    }
    let cc_addresses = $('#cc_addresses').val();
    if (cc_addresses !== '' && !email_validator(cc_addresses)) {
        alert('One of emails of cc addresses has incorrect pattern');return;
    }
    let step_ticket = $('#step_ticket').val();
    if (step_ticket === '') {
        alert('There is no free ticket now');return;
    }
    let reason = $('#reason').val();
    if (reason === '') {
        alert('Please fill the reason');return;
    }
    let priority_level = $('#priority_level').val();
    let start_date = $('#start_date').val();
    if (!datetime_validator(start_date)) {
        alert('Start date pattern is not correct');return;
    }
    let end_date = $('#end_date').val();
    if (!datetime_validator(end_date)) {
        alert('End date pattern is not correct');return;
    }
    let duration = $('#duration').val();
    if (duration === '') {
        alert('Duration is not calculated');return;
    }
    let splice_num = $('#splice_number').val();
    if (splice_num === '-1') {
        alert('Please select splice number');
        return;
    }
    let location = $('#location').val();
    let north = $('#ns_ord').val();
    let west = $('#we_ord').val();
    let circuit_ids = $('#circuit_id').val();
    if (circuit_ids.length === 0) {
        alert('There is no DF numbers matched');
        return;
    }
    let circuit_ids_ = JSON.stringify(circuit_ids);
    let param = {};
    param.to_addresses = to_addresses;
    param.cc_addresses = cc_addresses;
    param.ticket = step_ticket;
    param.reason = reason;
    param.priority = priority_level;
    param.start_date = start_date;
    param.end_date = end_date;
    param.duration = duration;
    param.splice_num = splice_num;
    param.location = location;
    param.north = north;
    param.west = west;
    param.circuit_ids = circuit_ids_;
    $.ajax({
       type: 'POST',
       url: '/submit_form',
       data: param,
       success: function (res) {
            if (res === 'success') {
                alert('Submitted!');
                window.location.reload();
            } else if (res ==='emailerror') {
                alert('Submitted! Sending email failed.');
                window.location.reload();
            }
            else {
                alert('Sorry, something went wrong.');return;
            }
       }
    });

}

function onclick_up_submit() {
    let to_addresses = $('#to_addresses').val();
    if (to_addresses === '') {
        alert('Please fill to addresses');return;
    }
    if (!email_validator(to_addresses)) {
        alert('One of emails of to addresses has incorrect pattern');return;
    }
    let cc_addresses = $('#cc_addresses').val();
    if (cc_addresses !== '' && !email_validator(cc_addresses)) {
        alert('One of emails of cc addresses has incorrect pattern');return;
    }
    let step_ticket = $('#step_ticket').val();
    if (step_ticket === '') {
        alert('There is no free ticket now');return;
    }
    let reason = $('#reason').val();
    if (reason === '') {
        alert('Please fill the reason');return;
    }
    let priority_level = $('#priority_level').val();
    let start_date = $('#start_date').val();
    if (!datetime_validator(start_date)) {
        alert('Start date pattern is not correct');return;
    }
    let end_date = $('#end_date').val();
    if (!datetime_validator(end_date)) {
        alert('End date pattern is not correct');return;
    }
    let duration = $('#duration').val();
    if (duration === '') {
        alert('Duration is not calculated');return;
    }
    let tk_status = $('#tk_status').val();
    let splice_num = $('#splice_number').val();
    if (splice_num === '-1') {
        alert('Please select splice number');
        return;
    }
    let location = $('#location').val();
    let north = $('#ns_ord').val();
    let west = $('#we_ord').val();
    let circuit_ids = $('#circuit_id').val();
    if (circuit_ids.length === 0) {
        alert('There is no DF numbers matched');
        return;
    }
    let circuit_ids_ = JSON.stringify(circuit_ids);
    let param = {};
    param.to_addresses = to_addresses;
    param.cc_addresses = cc_addresses;
    param.ticket = step_ticket;
    param.reason = reason;
    param.priority = priority_level;
    param.start_date = start_date;
    param.end_date = end_date;
    param.duration = duration;
    param.splice_num = splice_num;
    param.tk_status = tk_status;
    param.location = location;
    param.north = north;
    param.west = west;
    param.circuit_ids = circuit_ids_;
    $.ajax({
       type: 'POST',
       url: '/up_submit_form',
       data: param,
       success: function (res) {
            if (res === 'success') {
                alert('Submitted!');
                window.location.reload();
            } else if (res ==='emailerror') {
                alert('Submitted! Sending email failed.');
                window.location.reload();
            }
            else {
                alert('Sorry, something went wrong.');return;
            }
       }
    });
}

function onclick_cr_submit() {
    let to_addresses = $('#to_addresses').val();
    if (to_addresses === '') {
        alert('Please fill to addresses');return;
    }
    if (!email_validator(to_addresses)) {
        alert('One of emails of to addresses has incorrect pattern');return;
    }
    let cc_addresses = $('#cc_addresses').val();
    if (cc_addresses !== '' && !email_validator(cc_addresses)) {
        alert('One of emails of cc addresses has incorrect pattern');return;
    }
    let step_ticket = $('#step_ticket').val();
    if (step_ticket === '') {
        alert('There is no free ticket now');return;
    }
    let issue = $('#issue').val();
    if (issue === '') {
        alert('Please fill the issue');return;
    }
    let priority_level = $('#priority_level').val();
    let start_date = $('#start_date').val();
    if (!datetime_validator(start_date)) {
        alert('Start date pattern is not correct');return;
    }
    let splice_num = $('#splice_number').val();
    if (splice_num === '-1') {
        alert('Please select splice number');
        return;
    }
    let location = $('#location').val();
    let north = $('#ns_ord').val();
    let west = $('#we_ord').val();
    let circuit_ids = $('#circuit_id').val();
    if (circuit_ids.length === 0) {
        alert('There is no DF numbers matched');
        return;
    }
    let circuit_ids_ = JSON.stringify(circuit_ids);
    let param = {};
    param.to_addresses = to_addresses;
    param.cc_addresses = cc_addresses;
    param.ticket = step_ticket;
    param.issue = issue;
    param.priority = priority_level;
    param.start_date = start_date;
    param.splice_num = splice_num;
    param.location = location;
    param.north = north;
    param.west = west;
    param.circuit_ids = circuit_ids_;
    $.ajax({
       type: 'POST',
       url: '/cr_submit_form',
       data: param,
       success: function (res) {
            if (res === 'success') {
                alert('Submitted!');
                window.location.reload();
            } else if (res ==='emailerror') {
                alert('Submitted! Sending email failed.');
                window.location.reload();
            }
            else {
                alert('Sorry, something went wrong.');return;
            }
       }
    });
}

function onclick_ur_submit() {
    let to_addresses = $('#to_addresses').val();
    if (to_addresses === '') {
        alert('Please fill to addresses');return;
    }
    if (!email_validator(to_addresses)) {
        alert('One of emails of to addresses has incorrect pattern');return;
    }
    let cc_addresses = $('#cc_addresses').val();
    if (cc_addresses !== '' && !email_validator(cc_addresses)) {
        alert('One of emails of cc addresses has incorrect pattern');return;
    }
    let step_ticket = $('#step_ticket').val();
    if (step_ticket === '') {
        alert('There is no free ticket now');return;
    }
    let issue = $('#issue').val();
    if (issue === '') {
        alert('Please fill the issue');return;
    }
    let priority_level = $('#priority_level').val();
    let start_date = $('#start_date').val();
    if (!datetime_validator(start_date)) {
        alert('Start date pattern is not correct');return;
    }
    let end_date = $('#end_date').val();
    if (!datetime_validator(end_date)) {
        alert('End date pattern is not correct');return;
    }
    let duration = $('#duration').val();
    if (duration === '') {
        alert('Duration is not calculated');return;
    }
    let issue_resolution = $('#issue_resolution').val();
    if (issue_resolution === '') {
        alert('Please fill the resolution');return;
    }
    let splice_num = $('#splice_number').val();
    if (splice_num === '-1') {
        alert('Please select splice number');
        return;
    }
    let location = $('#location').val();
    let north = $('#ns_ord').val();
    let west = $('#we_ord').val();
    let circuit_ids = $('#circuit_id').val();
    if (circuit_ids.length === 0) {
        alert('There is no DF numbers matched');
        return;
    }
    let circuit_ids_ = JSON.stringify(circuit_ids);

    let param = {};
    param.to_addresses = to_addresses;
    param.cc_addresses = cc_addresses;
    param.ticket = step_ticket;
    param.issue = issue;
    param.priority = priority_level;
    param.start_date = start_date;
    param.end_date = end_date;
    param.duration = duration;
    param.splice_num = splice_num;
    param.location = location;
    param.north = north;
    param.west = west;
    param.circuit_ids = circuit_ids_;
    param.issue_resolution = issue_resolution;
    $.ajax({
       type: 'POST',
       url: '/ur_submit_form',
       data: param,
       success: function (res) {
            if (res === 'success') {
                alert('Submitted!');
                window.location.reload();
            } else if (res ==='emailerror') {
                alert('Submitted! Sending email failed.');
                window.location.reload();
            }
            else {
                alert('Sorry, something went wrong.');return;
            }
       }
    });
}

function onclick_edit_splice_point() {
    let param = {};
    param.splice_pt = $('#splice_number').val();
    param.chamber_id = $('#chamber_id').val();
    param.address = $('#address').val();
    param.ns_ord = $('#ns_ord').val();
    param.we_ord = $('#we_ord').val();
    $.ajax({
        type: 'POST',
        url: '/edit_splice_point',
        data: param,
        success: function (res) {
            if (res === 'success') {
                alert('Success');
                window.location.reload();
            } else {
                alert('Sorry, something went wrong.');return;
            }
        }
    });
}
function onclick_create_splice_point() {
    let param = {};
    param.splice_pt = $('#n_sp_num').val();
    param.chamber_id = $('#n_chamber_id').val();
    param.address = $('#n_address').val();
    param.ns_ord = $('#n_ns_ord').val();
    param.we_ord = $('#n_we_ord').val();
    $.ajax({
        type: 'POST',
        url: '/create_splice_point',
        data: param,
        success: function (res) {
            if (res === 'success') {
                alert('Success');
                window.location.reload();
            } else {
                alert('Sorry, something went wrong.');return;
            }
        }
    });
}
function onchange_splice_number_maintain_sp () {
    let splice_num = $('#splice_number').val();
    if (splice_num === '-1') {
        return;
    }
    let param = {'splice_num': splice_num};
    $('#auto_loading_fields').html('');
    $('#auto_loading_fields').load('/auto_load_sp', param);
}

function onclick_ribbon() {
    let ribbon_id = $('#ribbons').val();
    if (ribbon_id === '-1') {
        return;
    }
    for (var i=0;i < ribbons.length; i++) {
        if (ribbons[i]['id'] === ribbon_id){
            $('#fibrenolow').val(ribbons[i]['fibrenolow']);
            $('#fibrenohigh').val(ribbons[i]['fibrenohigh']);
        }
    }
}
function onclick_create_circuit() {
    let param = {};
    param.circuit = $('#circuit').val();
    param.ribbonid = $('#ribbons').val();
    param.ribbon_fibrenolow = $('#fibrenolow').val();
    param.ribbon_fibrenohigh = $('#fibrenohigh').val();
    param.splice_num = $('#splice_number').val();
    param.sp_a = $('#sp_a').is(':checked');
    param.sp_b = $('#sp_b').is(':checked');
    if (param.circuit === '') {
        alert('Please input circuit');
        return;
    }
    if (param.ribbonid === '-1') {
        alert('Please select ribbon');
        return;
    }
    if (param.splice_num === '-1') {
        alert('Please select splice number');
        return;
    }
    if (param.sp_a === false && param.sp_b === false) {
        alert('Check at least one of ends');return;
    }

    $.ajax({
        type: 'POST',
        url: '/create_circuit',
        data: param,
        success: function (res) {
            if (res === 'success') {
                alert('Success');
                window.location.reload();
            } else {
                alert('Sorry, something went wrong.');return;
            }
        }
    });

}

function onclick_search() {
    let param = {};
    param.from_dc = $('#from_dc').val();
    param.to_dc = $('#to_dc').val();
    $('#sp_pt_div').load('/load_search_from_to_dc', param);
}

function onchange_splice_query() {
    let param = {};
    param.sp = $('#splice_point').val();
    $('#sp_de_div').load('/load_sp_detail', param);
}

function onchange_circuit_query() {
    let param = {};
    param.circ = $('#circ').val();
    $('#cc_de_div').load('/load_cc_detail', param);
}