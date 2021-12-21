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

	$('.tab-sec a').on('click', function (e) {

		e.preventDefault();

		var $el = $(this),
			id = $el.attr('href');

		$('.hfc-outer section').removeClass('active');
		$('.tab-sec li').removeClass('active');
		$(id).addClass('active');
		$(this).parent().addClass('active');

		if (history.pushState) {
			history.pushState(null, null, id);
		}
		else {
			window.location.hash = id;
		}
	});

	function autoScroll() {
		var urlHash = window.location.hash;

		if (urlHash) {
			$('.hfc-outer section').removeClass('active');
			$('.tab-sec li').removeClass('active');
			$(urlHash).addClass('active');
			$('.tab-sec a[href="' + urlHash + '"]').parent().addClass('active');
		}

	}
	autoScroll();
});
