function ViewModel(){
    var self = this;
    self.medicineList = ko.observableArray();
    var url = $("table").attr("data-url");
    $.get(url, function(data){
        self.medicineList(data);
        console.log(self.medicineList())
    })

}

ko.applyBindings(new ViewModel());