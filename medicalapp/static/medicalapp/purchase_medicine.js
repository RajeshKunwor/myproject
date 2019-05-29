function Medicine(medi, quantity, manufacture_date, expiry_date){
    var self = this;
    self.medicineId = ko.observable(medi);
    self.rate = ko.observable();
    self.newRate = ko.pureComputed({
        read: function(){ self.rate(self.medicineId().rate);return self.medicineId().rate;},
        write: function(value){ self.rate(value);}


    });
    self.quantity = ko.observable(quantity);
    self.manufacture_date = ko.observable(manufacture_date);
    self.expiry_date = ko.observable(expiry_date);
    self.subTotal = ko.computed(function(){

       return self.rate()*self.quantity();
    });
}


function ViewModel(){

    var self = this;

    var url = $("form").attr("load-medicine");
    var saveurl = $("form").attr("action");
     self.medicineList = [];
     self.medicineA = [];
     self.medicinePurchaseArray = ko.observableArray();
     self.discount = ko.observable(0);

     $.get(url, function(data){
        self.medicineList = data;

        self.medicinePurchaseArray.push(new Medicine(self.medicineList[0],0,'',''));


    });


    self.add = function(){
        self.medicinePurchaseArray.push(new Medicine(self.medicineList[0],0,'',''));
    }

    self.remove = function(medicine){
        self.medicinePurchaseArray.remove(medicine);
    };

    self.save = function(){
        $.ajax(saveurl,{
            data: ko.toJSON({medicine_purchase: self.medicinePurchaseArray, discount: self.discount, netTotal: self.netTotal}),
            type: "post",
            success: function(response){ alert(response.response);}
        });
    };

    self.grandTotal = ko.computed(function(){
        var total = 0;
        $.each(self.medicinePurchaseArray(), function(){
            total+=this.subTotal();
        });
        return total;
    });

    self.netTotal = ko.computed(function(){
        var dis = self.discount();
        var disValue = dis/100*self.grandTotal();
        var netValue = self.grandTotal()-disValue;
        return netValue;

    });

}



ko.applyBindings(new ViewModel());

