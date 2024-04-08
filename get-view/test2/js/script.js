function searchAndRedirect() {
    var per = document.getElementById('searchinput').value;
    if (per !== '') {
        window.location.href = 'https://baike.baidu.com/item/' + per; // 替换为实际的网址
		// window.location.href = 'file:///C:/Users/HW/Desktop/人物关系系统/关系系统2.0/qianduan/renwu_dandu/' + per+'.html'; // 替换为实际的网址
    } else {
        // window.location.href = 'https://baike.baidu.com/item/' + per;
        alert('请输入您要查询的名字');
    }
}

