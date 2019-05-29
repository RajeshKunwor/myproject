function Medicine(medi){
    var self = this;

    self.name = ko.observable(medi.name);
    self.rate = ko.observable(medi.rate);
    self.description = ko.observable(medi.description)
}

var url = $("form").attr("action");
function ViewModel(){
    var self = this;

    self.name = ko.observable();
    self.rate = ko.observable();
    self.description = ko.observable();
    self.medicine = [{
        name: '',
        rate: '',
        description: ''
    }]
    self.medicineArray = ko.observableArray([new Medicine(self.medicine[0])]);

    self.add = function(){
        self.medicineArray.push(new Medicine({ name: self.name(), rate: self.rate(), description: self.description() }));
          console.log(self.medicineArray())
    };
    self.remove = function(md){
        self.medicineArray.remove(md);
      }

    self.save = function(){
        $.ajax(url,{
            data: ko.toJSON({ medicine: self.medicineArray}),
            type: "post",
            success: function(response){ alert(response.response); }
        });
    };

}

ko.applyBindings(new ViewModel());