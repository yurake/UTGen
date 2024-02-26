import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("UT Generator")

def test_mode_formatter(option):
    if option == "free":
        return "1.Free Format"
    elif option == "search_doc":
        return "2.ドキュメント検索"
    elif option == "gen_testcode":
        return "3.テストコード生成"
    elif option == "gen_utdoc":
        return "4.UT仕様書作成"
    elif option == "check_utdoc":
        return "5.UT仕様書校正"
    else:
        return option
    
def input_question(question):
    st.session_state.question = st.text_input("入力",question)

def upload_file():
    st.session_state.file = st.file_uploader("Choose a file", accept_multiple_files=True)
    if st.session_state.file is not None:
        st.write(st.session_state.file)

st.session_state.exec_mode = st.radio(
    "実行モード",
    options=["free", "search_doc", "gen_testcode", "gen_utdoc", "check_utdoc"],
    format_func=test_mode_formatter,
)

if st.session_state.exec_mode == "free":
    message = "聞きたいことを入力してください。"
elif st.session_state.exec_mode == "search_doc":
    message = "社内ドキュメントを検索します。検索したい内容を入力してください。"
elif st.session_state.exec_mode == "gen_testcode":
    message = "プロダクトコードをアップロードしてください"
elif st.session_state.exec_mode == "gen_utdoc":
    message = "詳細設計書をアップロードしてください"
elif st.session_state.exec_mode == "check_utdoc":
    message = "詳細設計書、プロダクトコード、テストコード、UT仕様書をアップロードしてください"

st.write(message)
if st.session_state.exec_mode == "free":
    input_question("JUnit5の使い方を、Junit4との違いに触れつつ教えてください。")
if st.session_state.exec_mode == "search_doc":
    input_question("データベースアクセス")
elif st.session_state.exec_mode == "gen_testcode" or st.session_state.exec_mode == "gen_utdoc" or st.session_state.exec_mode == "check_utdoc":
    upload_file()

if st.button('実行'):
    with st.spinner("実行中…"):
        time.sleep(3)
        st.write("---")
        if st.session_state.exec_mode == "free":
            response = """
            JUnit 5とJUnit 4は、Javaでのユニットテストを書くためのフレームワークですが、いくつかの重要な違いがあります。  
            JUnit 5はJUnitプラットフォームの一部であり、よりモダンなテスト機能とJava 8以上のサポートを提供します。  
            以下に、JUnit 5の使い方とJUnit 4との主な違いについて触れます。
            
            ## JUnit 5の主な特徴
            * **モジュール性**: JUnit 5はJUnit Platform、JUnit Jupiter、JUnit Vintageの3つの主要なサブプロジェクトから構成されています。  
            JUnit Platformはテストを実行するための基盤を提供し、JUnit JupiterはJUnit 5の新しいプログラミングモデルを提供し、JUnit Vintageは既存のJUnit 4ベースのテストの実行をサポートします。
            * **拡張モデル**: JUnit 5は、カスタム拡張を作成しやすい強力な拡張モデルを提供します。これにより、@Before/@Afterの注釈を使用する代わりに、より柔軟なテストライフサイクルのフックを実現できます。
            * **動的テスト**: JUnit 5では、実行時にプログラムによってテストケースを生成する動的テストをサポートしています。
            * **タグ付けとフィルタリング**: テストにタグを付け、特定のタグが付いたテストのみを実行する機能をサポートしています。
            
            ## JUnit 4との違い
            * **アノテーション**: JUnit 5では、テストクラスやメソッドを識別するためのアノテーションが変更されました。  
            例えば、@Testは両方で使用されますが、@BeforeEach、@AfterEach、@BeforeAll、@AfterAllはJUnit 5特有のものです（JUnit 4では@Before、@After、@BeforeClass、@AfterClass）。
            * **アサーション**: JUnit 5は、Assertionsクラスでより多くのアサーションメソッドを提供します。また、JUnit 5はJava 8のラムダ式をサポートし、アサーションの失敗メッセージを遅延評価できます。
            * **テストインスタンスのライフサイクル**: JUnit 5では、デフォルトで各テストメソッドごとに新しいテストインスタンスが作成されますが、これは設定で変更できます。
            * **パラメータ化テスト**: JUnit 5はパラメータ化テストをネイティブでサポートしており、より柔軟な方法でパラメータを提供できます。
            """
            st.write(response)
        elif st.session_state.exec_mode == "search_doc":
            response = pd.DataFrame({
                'ヒットした文章': ['Javaプログラムでのデータベースアクセスについて...', 'シェルスクリプトでのデータベースアクセスについて', '外部システムからのデータベースアクセスは許容していなく...'],
                'ドキュメント名': ['DBアクセス(Java)', 'DBアクセス(Shell)', 'アクセス制御'],
                '保存先': ['share/基本設計書/DBアクセス', 'share/基本設計書/DBアクセス', 'share/基本設計書/セキュリティ']
            })
            st.write(response)
        elif st.session_state.exec_mode == "gen_testcode":
            st.write("内容の正確性は保証されていません。実際にテストを実行し、期待される結果が得られることを確認してください。")
            response = """
            package webapp.tier.service;

            import static org.hamcrest.CoreMatchers.*;
            import static org.hamcrest.MatcherAssert.*;
            import static org.junit.jupiter.api.Assertions.*;

            import java.security.NoSuchAlgorithmException;
            import java.sql.Connection;
            import java.sql.DriverManager;
            import java.sql.SQLException;
            import java.sql.Statement;
            import java.util.ArrayList;
            import java.util.List;

            import javax.inject.Inject;

            import org.junit.jupiter.api.AfterEach;
            import org.junit.jupiter.api.BeforeEach;
            import org.junit.jupiter.api.Test;

            import io.quarkus.test.junit.QuarkusTest;
            import webapp.tier.bean.MsgBean;

            @QuarkusTest
            class MysqlServiceTest {

                @Inject
                MysqlService svc;

                String respbody = "Hello k8s-3tier-webapp with quarkus";

                @BeforeEach
                public void createTable() {
                    String createsql = "CREATE TABLE msg (id SERIAL PRIMARY KEY, msg TEXT NOT NULL)";
                    try (Connection con = DriverManager
                            .getConnection("jdbc:h2:tcp://localhost/mem:webapp;DB_CLOSE_DELAY=-1");
                            Statement stmt = con.createStatement()) {
                        stmt.executeUpdate(createsql);
                    } catch (SQLException e) {
                        e.fillInStackTrace();
                    }
                }

                @AfterEach
                public void dropTable() {
                    String createsql = "DROP TABLE msg";
                    try (Connection con = DriverManager
                            .getConnection("jdbc:h2:tcp://localhost/mem:webapp;DB_CLOSE_DELAY=-1");
                            Statement stmt = con.createStatement()) {
                        stmt.executeUpdate(createsql);
                    } catch (SQLException e) {
                        e.fillInStackTrace();
                    }
                }

                @Test
                void testConnectionStatusTrue() {
                    assertThat(svc.connectionStatus(), is(true));
                }

                @Test
                void testInsertMysql() {
                    try {
                        MsgBean bean = svc.insertMsg();
                        assertThat(bean.getFullmsg(), containsString(respbody));
                    } catch (SQLException | NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testInsertMysqlError() {
                    try {
                        dropTable();
                        svc.insertMsg();
                        fail();
                    } catch (Exception e) {
                        e.printStackTrace();
                        assertThat(e.getMessage(), is("Insert Error."));
                    }
                }

                @Test
                void testSelectMsgList10() {
                    try {
                        svc.invalidateCache();
                        List<Integer> expecteds = new ArrayList<>();
                        for (int i = 0; i < 10; i++) {
                            expecteds.add(svc.insertMsg().getId());
                        }
                        List<MsgBean> msgbeans = svc.selectMsg();
                        assertThat(msgbeans.size(), is(10));
                        msgbeans.forEach(s -> {
                            assertThat(s.getFullmsg(), containsString(respbody));
                            assertThat(expecteds.contains(s.getId()), is(true));
                        });
                    } catch (SQLException | NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testSelectMsgCache() {
                    try {
                        svc.invalidateCache();
                        int id = svc.insertMsg().getId();
                        svc.selectMsg();
                        dropTable();
                        List<MsgBean> msgbeans = svc.selectMsg();
                        msgbeans.forEach(s -> {
                            assertThat(s.getMessage(), containsString(respbody));
                            assertThat(s.getId(), is(id));
                        });
                    } catch (SQLException | NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testSelectMsgInvalidateCache() {
                    try {
                        int id = svc.insertMsg().getId();
                        svc.invalidateCache();
                        List<MsgBean> msgbeans = svc.selectMsg();
                        msgbeans.forEach(s -> {
                            assertThat(s.getMessage(), containsString(respbody));
                            assertThat(s.getId(), is(id));
                        });
                    } catch (SQLException | NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testSelectMsgNoData() {
                    try {
                        svc.invalidateCache();
                        List<MsgBean> msgbeans = svc.selectMsg();
                        msgbeans.forEach(s -> {
                            assertThat(s.getMessage(), is("No Data."));
                            assertThat(s.getId(), is(0));
                        });
                    } catch (SQLException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testSelectMsgError() {
                    try {
                        svc.invalidateCache();
                        dropTable();
                        svc.selectMsg();
                        fail();
                    } catch (SQLException e) {
                        e.printStackTrace();
                        assertEquals("Select Error.", e.getMessage());
                    }
                }

                @Test
                void testDeleteMsgNoData() {
                    try {
                        String recv = svc.deleteMsg();
                        assertThat(recv, is("Delete Msg Records"));
                    } catch (SQLException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testDeleteMsgWithData() {
                    try {
                        List<Integer> expecteds = new ArrayList<>();
                        for (int i = 0; i < 10; i++) {
                            expecteds.add(svc.insertMsg().getId());
                        }
                        String recv = svc.deleteMsg();
                        assertThat(recv, is("Delete Msg Records"));
                    } catch (SQLException | NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        fail();
                    }
                }

                @Test
                void testDeleteMsgError() {
                    try {
                        dropTable();
                        svc.deleteMsg();
                        fail();
                    } catch (SQLException e) {
                        e.printStackTrace();
                        assertEquals("Delete Error.", e.getMessage());
                    }
                }
            }
            """
            st.code(response)
        elif st.session_state.exec_mode == "gen_utdoc":
            response = pd.DataFrame({
                '名前': ['コネクション接続状態確認', 'データ挿入', 'データ挿入エラー'],
                'メソッド': ['testConnectionStatusTrue', 'testInsertMysql', 'testInsertMysqlError'],
                '期待値': ['DB接続状態が正常であること', 'データが挿入でき、入力データが全て含まれていること', 'データが挿入できないこと、エラーメッセージが返却されること'],
            })
            st.write(response)

        elif st.session_state.exec_mode == "check_utdoc":
            st.write("## サマリー")
            summary = pd.DataFrame({
                '項目': ['UT仕様書校正チェック', 'UT仕様書 - 詳細設計書 比較', 'UT仕様書 - テストコード 比較'],
                '結果': ['x', 'x', 'o'],
            })
            st.write(summary)

            time.sleep(3)
            response_edit = """
            ## UT仕様書校正チェック
            * シート: 処理機能記述書  
            x 処理が正常終了したい場合はコミットする。  
            o 処理が正常終了した場合はコミットする。  
            """
            st.write(response_edit)

            time.sleep(3)
            response_diff = """
            ## UT仕様書 - 詳細設計書 比較
            * 詳細設計書ではトランザクション数の上限値30を超える場合、エラーメッセージを返却する仕様になっているが、UT仕様書には記載がない。
            """
            st.write(response_diff)
