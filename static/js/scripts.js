$(document).ready(function () {
	$('.menu-btn').click(function () {
		$(this).toggleClass('active');
		$('.header__right').slideToggle();
	});

	if ($('#datepicker').length > 0) {
		$("#datepicker").datepicker({
			dateFormat: "dd-mm-yy"
		});
	}

	if (window.location.hash) {
		if ($(window.location.hash).length > 0) {
			$('.tab-sec li').removeClass('active');
			$('a[href="' + window.location.hash + '"]').parent().addClass('active');

			$('.hfc-outer section').removeClass('active');
			$(window.location.hash).addClass('active');
		}
	}

	function autoScroll() {
		$('.tab-sec a').on('click', function (e) {
			e.preventDefault();

			var $el = $(this),
				id = $el.attr('href');

			$('.hfc-outer section').removeClass('active');
			$('.tab-sec li').removeClass('active');
			$(id).addClass('active');
			$(this).parent().addClass('active');
		});
	}
	autoScroll();
});
