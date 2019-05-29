function ViewModel(){
    var self = this;
    //hospital observable
    self.hospitalName = ko.observable();
    self.address = ko.observable();
    self.email = ko.observable();
    self.phone = ko.observable();

    //medicine obercable
    self.medicineName = ko.observable();
    self.quantity = ko.observable();
    self.expiry_date = ko.observable();
    self.manufacture_date = ko.observable();
    self.created_date = ko.observable();
    self.updated_date = ko.observable();
    self.medicineArray = ko.observableArray();
    var hostipalUrl = '';
    var medicineUrl = $("form").attr("action");
//    self.saveHospital = function(){
//
//        $.ajax(hostipalUrl,{
//            data: { name: self.hospitalName, address: self.address, email: self.email, phone: self.phone},
//            type = "post",
//            success:{function(response){alert(response.response);}}
//        };
//    )};


    self.saveMedicine = function(){
        console.log(ko.toJSON({ medicine: self.medicineArray }));
        $.ajax(medicineUrl,{
            data: ko.toJSON({ medicine: self.medicineArray }),
            type: "post",
            success: {function(response){ alert(response.response); }}
        });
    };

    self.add = function(){
        self.medicineArray.push({ name: self.medicineName(),
        quantity: self.quantity(), manufacture_date: self.manufacture_date(),
        expiry_date: self.expiry_date() });
        console.log(self.medicineArray())

    };

    self.remove = function(medicine){

        self.medicineArray.remove(medicine)
    }
}

ko.applyBindings(new ViewModel());