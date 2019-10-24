// Generated from UP2OB.g4 by ANTLR 4.7.1

	package se.cth.pursue;

   import java.util.Set;
   import java.util.HashSet;

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link UP2OBParser}.
 */
public interface UP2OBListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link UP2OBParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(UP2OBParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2OBParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(UP2OBParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2OBParser#declaration_block}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration_block(UP2OBParser.Declaration_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2OBParser#declaration_block}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration_block(UP2OBParser.Declaration_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2OBParser#machine_block}.
	 * @param ctx the parse tree
	 */
	void enterMachine_block(UP2OBParser.Machine_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2OBParser#machine_block}.
	 * @param ctx the parse tree
	 */
	void exitMachine_block(UP2OBParser.Machine_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2OBParser#location_block}.
	 * @param ctx the parse tree
	 */
	void enterLocation_block(UP2OBParser.Location_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2OBParser#location_block}.
	 * @param ctx the parse tree
	 */
	void exitLocation_block(UP2OBParser.Location_blockContext ctx);
	/**
	 * Enter a parse tree produced by {@link UP2OBParser#transition_block}.
	 * @param ctx the parse tree
	 */
	void enterTransition_block(UP2OBParser.Transition_blockContext ctx);
	/**
	 * Exit a parse tree produced by {@link UP2OBParser#transition_block}.
	 * @param ctx the parse tree
	 */
	void exitTransition_block(UP2OBParser.Transition_blockContext ctx);
}