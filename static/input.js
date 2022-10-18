$("input[data-type='currency']").on({
    keyup: function() {
      formatCurrency($(this));
      
    },
    blur: function() { 
      formatCurrency($(this), "blur");
    }
});

function formatNumber(n) {
  //Format number 
  //Add decimal on blur, add commas, remove invalid characters
  return n.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

function formatCurrency(input, blur) {
  //Validates decimal side
  //and puts cursor back in right position.

  //Get input value
  var input_val = input.val();
  
  //Input was empty
  if (input_val === "") { return; }

  var decimal_pos = input_val.indexOf(".");

  //Split number by decimal point
  var left_side = input_val.substring(0, decimal_pos);

  //Limit user input
  if (left_side > 1000000) {
    input_val = input_val.substring(0, input_val.length-1);
  }
  
  //Original length
  var original_len = input_val.length;

  //If last character comma, remove it
  if (original_len-1 === ",") {
    input_val = input_val.slice(0, -1);
  }

  //Initial caret position 
  var caret_pos = input.prop("selectionStart");
    
  //Check for decimal
  if (input_val.indexOf(".") >= 0) {

    //Get position of first decimal
    //Stop multiple decimals from being entered
    var decimal_pos = input_val.indexOf(".");

    //Split number by decimal point
    var left_side = input_val.substring(0, decimal_pos);
    var right_side = input_val.substring(decimal_pos);

    //Add commas to left side
    left_side = formatNumber(left_side);

    //Validate right side
    right_side = formatNumber(right_side);
    
    //On blur make sure 2 numbers after decimal
    if (blur === "blur") {
      right_side += "00";
    }
    
    //Limit decimal to only 2 digits
    right_side = right_side.substring(0, 2);

    //Join both sides by a decimal
    input_val = left_side + "." + right_side;

  } else {
    //No decimal in input
    //Add commas to number
    //Remove all non-digits
    input_val = formatNumber(input_val);
    
    //Final formatting
    if (blur === "blur") {
      input_val += ".00";
    }
  }
  
  //Send updated string to input
  input.val(input_val);

  //Put caret back in position
  var updated_len = input_val.length;
  caret_pos = updated_len - original_len + caret_pos;
  input[0].setSelectionRange(caret_pos, caret_pos);
}