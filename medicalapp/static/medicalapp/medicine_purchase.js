function ViewModel(){
    var self = this;
    self.medicinePurchaseList = ko.observableArray();
    var url = $("table").attr("data-url");
    $.get(url, function(data){
        self.medicinePurchaseList(data);
    });
}
ko.applyBindings(new ViewModel());