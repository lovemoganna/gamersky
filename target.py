import json
import re


html = ''' 
<div class="movies-list">

    <dl class="movie-list">
        <dd>
            <div class="movie-item">
                <a href="/films/588362" target="_blank" data-act="movie-click" data-val="{movieid:588362}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/aeb864fa21d578d845b9cefc056e40cb2874891.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="摔跤吧！爸爸">
                <a href="/films/588362" target="_blank" data-act="movies-click" data-val="{movieId:588362}">摔跤吧！爸爸</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">8</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/344264" target="_blank" data-act="movie-click" data-val="{movieid:344264}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/02ac72c0e8ee2987f7662ad921a2acc7999433.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax2d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="战狼2">
                <a href="/films/344264" target="_blank" data-act="movies-click" data-val="{movieId:344264}">战狼2</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">7</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/342068" target="_blank" data-act="movie-click" data-val="{movieid:342068}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/14f9018b371d94dd812772704613babd475457.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="寻梦环游记">
                <a href="/films/342068" target="_blank" data-act="movies-click" data-val="{movieId:342068}">寻梦环游记</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/343136" target="_blank" data-act="movie-click" data-val="{movieid:343136}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/f042762fa4a975501b69d4f6af6520341035964.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="小萝莉的猴神大叔">
                <a href="/films/343136" target="_blank" data-act="movies-click" data-val="{movieId:343136}">小萝莉的猴神大叔</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/78405" target="_blank" data-act="movie-click" data-val="{movieid:78405}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/b22bc4b0cf71916e6c2f4c335c3a66a0300236.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="速度与激情7">
                <a href="/films/78405" target="_blank" data-act="movies-click" data-val="{movieId:78405}">速度与激情7</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1203" target="_blank" data-act="movie-click" data-val="{movieid:1203}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="霸王别姬">
                <a href="/films/1203" target="_blank" data-act="movies-click" data-val="{movieId:1203}">霸王别姬</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/6823" target="_blank" data-act="movie-click" data-val="{movieid:6823}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/7/2144189.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="大话西游之月光宝盒">
                <a href="/films/6823" target="_blank" data-act="movies-click" data-val="{movieId:6823}">大话西游之月光宝盒</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1187517" target="_blank" data-act="movie-click" data-val="{movieid:1187517}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/f34b13e6f79c6d736ffbf996b1f60267374252.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="火力全开">
                <a href="/films/1187517" target="_blank" data-act="movies-click" data-val="{movieId:1187517}">火力全开</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/410681" target="_blank" data-act="movie-click" data-val="{movieid:410681}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/81e83b091c51c0ff11221e48a202d6a4100328.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="BIGBANG MADE">
                <a href="/films/410681" target="_blank" data-act="movies-click" data-val="{movieId:410681}">BIGBANG
                    MADE</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/342291" target="_blank" data-act="movie-click" data-val="{movieid:342291}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/00b7688f72aeabd35f10ff61de4ed224255881.png@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="在刺刀和藩篱下">
                <a href="/films/342291" target="_blank" data-act="movies-click" data-val="{movieId:342291}">在刺刀和藩篱下</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">6</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1182552" target="_blank" data-act="movie-click" data-val="{movieid:1182552}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/82a01e8f773c273ba10b96b5acb06196381700.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="红海行动">
                <a href="/films/1182552" target="_blank" data-act="movies-click" data-val="{movieId:1182552}">红海行动</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1208122" target="_blank" data-act="movie-click" data-val="{movieid:1208122}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/4b87b0c8ec1df5ec8de2781b017e255780815.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="神秘巨星">
                <a href="/films/1208122" target="_blank" data-act="movies-click" data-val="{movieId:1208122}">神秘巨星</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/246286" target="_blank" data-act="movie-click" data-val="{movieid:246286}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/9c79f4791bff2f85f1fd2a3ab09bc8e9358164.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="疯狂动物城">
                <a href="/films/246286" target="_blank" data-act="movies-click" data-val="{movieId:246286}">疯狂动物城</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/4055" target="_blank" data-act="movie-click" data-val="{movieid:4055}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/fc9d78dd2ce84d20e53b6d1ae2eea4fb1515304.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="这个杀手不太冷">
                <a href="/films/4055" target="_blank" data-act="movies-click" data-val="{movieId:4055}">这个杀手不太冷</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/78410" target="_blank" data-act="movie-click" data-val="{movieid:78410}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/69ace6938ad009085532130651e3dc7f306844.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="冰雪奇缘">
                <a href="/films/78410" target="_blank" data-act="movies-click" data-val="{movieId:78410}">冰雪奇缘</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/267" target="_blank" data-act="movie-click" data-val="{movieid:267}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/11/324629.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="泰坦尼克号">
                <a href="/films/267" target="_blank" data-act="movies-click" data-val="{movieId:267}">泰坦尼克号</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1297" target="_blank" data-act="movie-click" data-val="{movieid:1297}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="肖申克的救赎">
                <a href="/films/1297" target="_blank" data-act="movies-click" data-val="{movieId:1297}">肖申克的救赎</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/79232" target="_blank" data-act="movie-click" data-val="{movieid:79232}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/7d633fc3c0b4603b214ab762a1e0f470361756.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="超能陆战队">
                <a href="/films/79232" target="_blank" data-act="movies-click" data-val="{movieId:79232}">超能陆战队</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/78099" target="_blank" data-act="movie-click" data-val="{movieid:78099}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/d5e5e53ef9bbd98223e83df261b51b84103223.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="疯狂原始人">
                <a href="/films/78099" target="_blank" data-act="movies-click" data-val="{movieId:78099}">疯狂原始人</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">5</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/458721" target="_blank" data-act="movie-click" data-val="{movieid:458721}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/45a9dfd545596669fc742bca0d3dc5512642616.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="看不见的客人">
                <a href="/films/458721" target="_blank" data-act="movies-click" data-val="{movieId:458721}">看不见的客人</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/78018" target="_blank" data-act="movie-click" data-val="{movieid:78018}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p1.meituan.net/movie/2b0a4b01d0c9f70ae265da7bf2d3c649357286.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="魁拔Ⅲ战神崛起">
                <a href="/films/78018" target="_blank" data-act="movies-click" data-val="{movieId:78018}">魁拔Ⅲ战神崛起</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/125" target="_blank" data-act="movie-click" data-val="{movieid:125}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/85/637119.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="泰坦尼克号3D">
                <a href="/films/125" target="_blank" data-act="movies-click" data-val="{movieId:125}">泰坦尼克号3D</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/78341" target="_blank" data-act="movie-click" data-val="{movieid:78341}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/a0c0212013afeb61492200722355fca925301.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax2d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="星际穿越">
                <a href="/films/78341" target="_blank" data-act="movies-click" data-val="{movieId:78341}">星际穿越</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1633" target="_blank" data-act="movie-click" data-val="{movieid:1633}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img src="http://p0.meituan.net/movie/53/1541925.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="阿甘正传">
                <a href="/films/1633" target="_blank" data-act="movies-click" data-val="{movieId:1633}">阿甘正传</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/249198" target="_blank" data-act="movie-click" data-val="{movieid:249198}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img data-src="http://p1.meituan.net/movie/67c91a4a738444f46be451313f6c9ff78639306.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="启功">
                <a href="/films/249198" target="_blank" data-act="movies-click" data-val="{movieId:249198}">启功</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/78326" target="_blank" data-act="movie-click" data-val="{movieid:78326}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img data-src="http://p1.meituan.net/movie/acd6df2fa2fa2bac1384cc25be4d8501415556.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="m3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="5月天诺亚方舟">
                <a href="/films/78326" target="_blank" data-act="movies-click" data-val="{movieId:78326}">5月天诺亚方舟</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/248700" target="_blank" data-act="movie-click" data-val="{movieid:248700}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img data-src="http://p0.meituan.net/movie/9f61bf914c6881b4d1d297ddef796a62207111.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"><i class="imax3d"></i></div>
            </div>
            <div class="channel-detail movie-item-title" title="速度与激情8">
                <a href="/films/248700" target="_blank" data-act="movies-click" data-val="{movieId:248700}">速度与激情8</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">3</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/246082" target="_blank" data-act="movie-click" data-val="{movieid:246082}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img data-src="http://p0.meituan.net/movie/04fd9542cb749fc824190933feacc5b0294181.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="夏洛特烦恼">
                <a href="/films/246082" target="_blank" data-act="movies-click" data-val="{movieId:246082}">夏洛特烦恼</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">3</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/672130" target="_blank" data-act="movie-click" data-val="{movieid:672130}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img data-src="http://p0.meituan.net/movie/862563dfea65ac947a149ce466f7f1771014432.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="奇迹男孩">
                <a href="/films/672130" target="_blank" data-act="movies-click" data-val="{movieId:672130}">奇迹男孩</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">3</i></div>

        </dd>
        <dd>
            <div class="movie-item">
                <a href="/films/1198177" target="_blank" data-act="movie-click" data-val="{movieid:1198177}">
                    <div class="movie-poster">
                        <img class="poster-default" src="//ms0.meituan.net/mywww/image/loading_2.e3d934bf.png">
                        <img data-src="http://p1.meituan.net/movie/cff7012c0cc944b27c9bba352a785e8e358408.jpg@160w_220h_1e_1c">
                    </div>
                </a>

                <div class="movie-ver"></div>
            </div>
            <div class="channel-detail movie-item-title" title="缝纫机乐队">
                <a href="/films/1198177" target="_blank" data-act="movies-click" data-val="{movieId:1198177}">缝纫机乐队</a>
            </div>
            <div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">3</i></div>

        </dd>
    </dl>


</div>
'''
# 2.正则表达式解析
result = re.findall (
    '<dd.*?movie-item.*?movie-poster.*?<img\ssrc="(.*?)".*?movie-item-title.*?<a.*?data-val="(.*?)">(.*?)</a>.*?channel-detail-orange.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
    html, re.S)


# print(type(result)) # <class 'list'>

# list 类型的提取是用for循环就可以,但是是惰性提取.

# print(list(i for i in result)) # 先变成了一个生成器,然后再用list打印出就可以了.

# print(result[0]) # 这是一个Tuple,无法更改.
# print()

# for i in result:
#      image,movieId,movieTitle,alexa,a = i
#      print('海报',image,'电影编号',movieId,'电影名',movieTitle,'评分',alexa,'a',a)

# 3.以字典形式解析HTML
def parse_one_page(result):
    for r in result:
        yield {'haibao': r[0], 'movieId': r[1], 'movieTitle': r[2], 'Alexa': r[3] + r[4]}

# 4.写到文件里面去

def write_to_file(content):
    # 写入到一个文件
    with open('result.txt','a',encoding='UTF-8') as f:
        # 通过json转为字符串的形式存储,后面是为了解决编码问题.
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()


def main():
    for item in parse_one_page (result):
        print (item)
        write_to_file(item)

if __name__ == '__main__':
    main ()
