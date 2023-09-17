import { FormControl, ValidationErrors } from "@angular/forms";

export class FormValidators {

    // whitespace validators
    static notOnlyWhitespace(control:FormControl):ValidationErrors{
        //check if string only contains whitespace
        if( (control.value != null) && (control.value.trim().length === 0)  ){
            //invalid, return error object
            return{'notOnlyWhitespace':true};
        }
        else{
            return null;
        }
        
        
        return null;
    }




}
