$(document).ready(function() {
    // Create an empty object to store amenities with their status (checked or unchecked)
    const amenities = {};

    // Listen for changes on all input checkboxes
    $('input[type=checkbox]').change(function() {
        // Get the 'data-name' attribute of the changed checkbox, which represents the amenity_id
        const amenityName = $(this).data('name');

        // Check if the checkbox is checked
        if ($(this).is(':checked')) {
            // If checked, set the amenity_id as a property in the 'amenities' object with a value of 'true'
            amenities[amenityName] = true;
        } else {
            // If unchecked, remove the amenity_id from the 'amenities' object
            delete amenities[amenityName];
        }

        // Get the list of selected amenities
        const selectedAmenities = Object.keys(amenities);

        // Update the text inside the <h4> tag within the 'div.amenities' with the updated list of selected amenities
        $('div.amenities h4').text(selectedAmenities.join(', '));
    });
});
