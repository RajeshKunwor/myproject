function ViewModel(){
    var self = this;
    self.medicineData = ko.observableArray();
    var url = $("table").attr("data-url");
    $.get(url, function(data){
        self.medicineData(data);

    });

}
ko.applyBindings(new ViewModel())