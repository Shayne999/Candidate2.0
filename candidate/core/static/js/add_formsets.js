document.addEventListener('DOMContentLoaded', function() {
    // Function to handle dynamic formset addition
    function addDynamicFormset(buttonId, formsetPrefix, totalFormsId, formRowClass, containerId, removeBtnClass) {
        let formIndex = document.getElementById(totalFormsId).value;

        document.getElementById(buttonId).addEventListener('click', function() {
            // Clone the last form
            let newForm = document.querySelector(`.${formRowClass}`).cloneNode(true);
            newForm.innerHTML = newForm.innerHTML.replace(/__prefix__/g, formIndex);

            // Clear input fields
            newForm.querySelectorAll('input').forEach(input => {
                if (input.type === 'hidden' && input.name.includes('id')) {
                    input.value = '';
                } else {
                    input.value = '';
                }
            });

            newForm.querySelectorAll('textarea').forEach(textarea => textarea.value = '');
            newForm.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

            // Update name and id attributes
            newForm.querySelectorAll('[name], [id]').forEach(element => {
                if (element.name) {
                    element.name = element.name.replace(/-\d+-/, `-${formIndex}-`);
                }
                if (element.id) {
                    element.id = element.id.replace(/-\d+-/, `-${formIndex}-`);
                }
            });


            // Inserts new forms above the add button/icon
            let formsetContainer = document.getElementById(containerId);
            let addButton = document.getElementById(buttonId);
            formsetContainer.insertBefore(newForm, addButton);

            // Increment the formset index and update the management form's total form count
            formIndex++;
            document.getElementById(totalFormsId).value = formIndex;

            // Add remove button handler for the new form
            handleRemoveButton(newForm.querySelector(`.${removeBtnClass}`));
        });
    }

    // Function to handle formset removal
    function handleRemoveButton(removeButton, formsetRowClass) {
        removeButton.addEventListener('click', function() {
            let formRow = removeButton.closest(`.${formsetRowClass}`);
            formRow.style.display = 'none';
            let deleteCheckbox = formRow.querySelector('input[type="checkbox"][name$="-DELETE"]');
            if (deleteCheckbox) {
                deleteCheckbox.checked = true;
            }
        });
    }

    // Add remove button to existing formsets
    function initializeRemoveButtons(removeBtnClass, formsetRowClass) {
        document.querySelectorAll(`.${removeBtnClass}`).forEach(function(removeButton) {
            handleRemoveButton(removeButton, formsetRowClass);
        });
    }

    // Add new formsets
    addDynamicFormset('add-work-experience', 'work_experience', 'id_work_experience-TOTAL_FORMS', 'experience-formset-row', 'work-experience-container', 'remove-work-experience');
    addDynamicFormset('add-education', 'education', 'id_education-TOTAL_FORMS', 'education-formset-row', 'education-container', 'remove-education');
    addDynamicFormset('add-project', 'project', 'id_projects-TOTAL_FORMS', 'project-formset-row', 'project-container', 'remove-project');
    addDynamicFormset('add-skill', 'skill', 'id_skills-TOTAL_FORMS', 'skills-formset-row', 'skills-container', 'remove-skill');
    addDynamicFormset('add-language', 'language', 'id_languages-TOTAL_FORMS', 'language-formset-row', 'languages-container', 'remove-language');
    addDynamicFormset('add-reference', 'reference', 'id_references-TOTAL_FORMS', 'reference-formset-row', 'references-container', 'remove-reference');
    addDynamicFormset('add-additional-info', 'additional_info', 'id_additional_info-TOTAL_FORMS', 'additional-info-formset-row', 'additional-info-container', 'remove-additional-info');

    // Remove buttons
    initializeRemoveButtons('remove-work-experience', 'experience-formset-row');
    initializeRemoveButtons('remove-education', 'education-formset-row');
    initializeRemoveButtons('remove-project', 'project-formset-row');
    initializeRemoveButtons('remove-skill', 'skills-formset-row');
    initializeRemoveButtons('remove-language', 'language-formset-row');
    initializeRemoveButtons('remove-reference', 'reference-formset-row');
    initializeRemoveButtons('remove-additional-info', 'additional-info-formset-row');
});
